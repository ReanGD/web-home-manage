import { Component, OnInit  } from '@angular/core';
import { RemoteTorrentsService, RemoteTorrent } from './remoteTorrents.service';
import { SelectItem} from 'primeng/primeng';

import 'style-loader!./remoteTorrents.scss';

@Component({
  selector: 'remote-torrents-table',
  templateUrl: 'remoteTorrents.table.html',
})

export class RemoveTorrentsTable implements OnInit {

  torrents: RemoteTorrent[];
  content_type: SelectItem[];

  constructor(private service: RemoteTorrentsService) { }

  ngOnInit() {
    this.content_type = [];
    this.content_type.push({label: 'All', value: null});
    this.content_type.push({label: 'Films', value: 'Films'});
    this.content_type.push({label: 'AudioBooks', value: 'AudioBooks'});
    this.content_type.push({label: 'Serials', value: 'Serials'});
    this.content_type.push({label: 'Others', value: 'Others'});

    this.service.getRemoteTorrents().then(torrents => this.torrents = torrents);
  }
}
