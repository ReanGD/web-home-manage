import {NgModule}      from '@angular/core';
import {CommonModule}  from '@angular/common';
import {NgaModule} from '../../theme/nga.module';
import {RatingModule} from 'ng2-bootstrap';
import {DataTableModule, SharedModule, DropdownModule} from 'primeng/primeng';

import {routing} from './torrents.routing';
import {Torrents} from './torrents.component';
import {RemotesTable} from './components/remotes/remotes.component';
import {RemotesService} from './components/remotes/remotes.service';
import {LocalsTable} from './components/locals/locals.component';
import {LocalsService} from './components/locals/locals.service';

@NgModule({
  imports: [
    CommonModule,
    NgaModule,
    RatingModule.forRoot(),
    routing,

    SharedModule,
    DataTableModule,
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
