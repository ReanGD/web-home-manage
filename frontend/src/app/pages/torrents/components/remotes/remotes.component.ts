import {Component, OnInit} from '@angular/core';
import {RemotesService, Remotes} from './remotes.service';
import {Message, SelectItem} from "primeng/components/common/api";

import 'style-loader!./remotes.scss';

@Component({
  selector: 'remotes-table',
  templateUrl: 'remotes.table.html',
})

export class RemotesTable implements OnInit {

  msgs: Message[] = [];
  torrents: Remotes[];
  content_type: SelectItem[];

  constructor(private service: RemotesService) {
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
    this.service.get()
      .then(torrents => { this.torrents = torrents; return torrents.length; })
      .then(len => this.msgs.push(
        { severity: 'success', summary: 'Load success', detail: len + ' torrents' }));
  }
}
