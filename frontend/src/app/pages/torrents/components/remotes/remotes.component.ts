import {Component, OnInit} from '@angular/core';
import {TorrentsService, Remote, Local} from '../../torrents.service';
import {Message, SelectItem} from "primeng/components/common/api";


@Component({
  selector: 'remotes-table',
  templateUrl: 'remotes.table.html',
})

export class RemotesTable implements OnInit {

  msgs: Message[] = [];
  torrents: Remote[];
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
    this.service.getRemotes()
      .then(torrents => { this.torrents = torrents; return torrents.length; })
      .then(len => this.msgs.push(
        { severity: 'success', summary: 'Load success', detail: len + ' torrents' }));
  }

  downloadTorrent(torrent: Remote) {
    this.service.createLocal(torrent);
  }
}
