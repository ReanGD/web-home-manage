import {NgModule}      from '@angular/core';
import {CommonModule}  from '@angular/common';
import {NgaModule} from '../../theme/nga.module';
import {RatingModule} from 'ng2-bootstrap';
import {DataTableModule, SharedModule, DropdownModule,
  ButtonModule, GrowlModule, ConfirmDialogModule} from 'primeng/primeng';

import {routing} from './torrents.routing';
import {Torrents} from './torrents.component';
import {TorrentsService} from './torrents.service';
import {RemotesTable} from './components/remotes/remotes.component';
import {LocalsTable} from './components/locals/locals.component';

@NgModule({
  imports: [
    CommonModule,
    NgaModule,
    RatingModule.forRoot(),
    routing,

    SharedModule,
    DataTableModule,
    DropdownModule,
    ButtonModule,
    GrowlModule,
    ConfirmDialogModule,
  ],
  declarations: [
    Torrents,
    RemotesTable,
    LocalsTable,
  ],
  providers: [
    TorrentsService,
  ]
})
export class TorrentsModule {
}
