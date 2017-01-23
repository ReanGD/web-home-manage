import {NgModule}      from '@angular/core';
import {DataTableModule, SharedModule, DropdownModule} from 'primeng/primeng';

import {routing} from './torrents.routing';
import {Torrents} from './torrents.component';
import {RemotesTable} from './components/remotes/remotes.component';
import {RemotesService} from './components/remotes/remotes.service';

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
  ],
  providers: [
    RemotesService,
  ]
})
export class TorrentsModule {
}
