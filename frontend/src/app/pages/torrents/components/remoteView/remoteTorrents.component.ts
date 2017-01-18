import { Component, OnInit  } from '@angular/core';
import { RemoteTorrentsService, RemoteTorrent } from './remoteTorrents.service';

import 'style-loader!./remoteTorrents.scss';

@Component({
  selector: 'remote-torrents-table',
  templateUrl: 'remoteTorrents.table.html',
})

export class RemoveTorrentsTable implements OnInit {

  torrents: RemoteTorrent[];

  constructor(private service: RemoteTorrentsService) { }

  ngOnInit() {
      this.service.getRemoteTorrents().then(torrents => this.torrents = torrents);
  }
}
