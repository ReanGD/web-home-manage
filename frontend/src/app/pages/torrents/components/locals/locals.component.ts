import {Component, OnInit} from '@angular/core';
import {TorrentsService, Local} from '../../torrents.service';
import {Message, SelectItem} from "primeng/components/common/api";


@Component({
  selector: 'locals-table',
  templateUrl: 'locals.table.html',
})

export class LocalsTable implements OnInit {

  msgs: Message[] = [];
  torrents: Local[];
  content_type: SelectItem[];

  constructor(private service: TorrentsService) {
  }

  ngOnInit() {
    this.content_type = [];
    this.content_type.push({label: 'All', value: null});
    this.content_type.push({label: 'Films', value: 'Films'});
    this.content_type.push({label: 'AudioBooks', value: 'AudioBooks'});
    this.content_type.push({label: 'Serials', value: 'Serials'});
    this.content_type.push({label: 'Others', value: 'Others'});

    this.refreshTable();
  }

  refreshTable() {
    this.service.getLocals()
      .then(torrents => { this.torrents = torrents; return torrents.length; })
      .then(len => this.msgs.push(
        { severity: 'success', summary: 'Load success', detail: len + ' torrents.' }));
  }

  removeTorrent(torrents: Local) {
    this.service.removeLocal(torrents)
      .then(() => this.refreshTable());
  }
}
