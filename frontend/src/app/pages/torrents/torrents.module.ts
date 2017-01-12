import {NgModule}      from '@angular/core';
import {DataTableModule, SharedModule} from 'primeng/primeng';

import {routing} from './torrents.routing';
import {Torrents} from './torrents.component';
import {RemoveTorrentsTable} from './components/remoteView/remoteTorrents.component';
import {RemoteTorrentsService} from './components/remoteView/remoteTorrents.service';

@NgModule({
  imports: [
    routing,
    DataTableModule,
    SharedModule,
  ],
  declarations: [
    Torrents,
    RemoveTorrentsTable,
  ],
  providers: [
    RemoteTorrentsService,
  ]
})
export class TorrentsModule {
}
