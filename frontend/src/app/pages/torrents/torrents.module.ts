import {NgModule}      from '@angular/core';
import {DataTableModule, SharedModule, DropdownModule} from 'primeng/primeng';

import {routing} from './torrents.routing';
import {Torrents} from './torrents.component';
import {RemotesTable} from './components/remotes/remotes.component';
import {RemotesService} from './components/remotes/remotes.service';
import {LocalsTable} from './components/locals/locals.component';
import {LocalsService} from './components/locals/locals.service';

@NgModule({
  imports: [
    routing,
    DataTableModule,
    SharedModule,
    DropdownModule,
  ],
  declarations: [
    Torrents,
    RemotesTable,
    LocalsTable,
  ],
  providers: [
    RemotesService,
    LocalsService,
  ]
})
export class TorrentsModule {
}
