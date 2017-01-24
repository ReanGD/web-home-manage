import { Component, OnInit  } from '@angular/core';
import { LocalsService, Locals } from './locals.service';
import { SelectItem } from 'primeng/primeng';

import 'style-loader!./locals.scss';

@Component({
  selector: 'locals-table',
  templateUrl: 'locals.table.html',
})

export class LocalsTable implements OnInit {

  torrents: Locals[];
  content_type: SelectItem[];

  constructor(private service: LocalsService) { }

  ngOnInit() {
    this.content_type = [];
    this.content_type.push({label: 'All', value: null});
    this.content_type.push({label: 'Films', value: 'Films'});
    this.content_type.push({label: 'AudioBooks', value: 'AudioBooks'});
    this.content_type.push({label: 'Serials', value: 'Serials'});
    this.content_type.push({label: 'Others', value: 'Others'});

    this.service.get().then(torrents => this.torrents = torrents );
  }
}
