import { NgModule }      from '@angular/core';
import { CommonModule }  from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgaModule } from '../../theme/nga.module';
import { Ng2SmartTableModule } from 'ng2-smart-table';

// import {AccordionModule} from 'primeng/primeng';
import {DataTableModule,SharedModule} from 'primeng/primeng';

import { routing }       from './torrents.routing';
import { Tables } from './torrents.component';
import { BorderedTable } from './components/remoteView/remoteView.component';
import { BasicTablesService } from './components/remoteView/remoteView.service';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    NgaModule,
    routing,
    Ng2SmartTableModule,
    DataTableModule,
    SharedModule,
  ],
  declarations: [
    Tables,
    BorderedTable,
  ],
  providers: [
    BasicTablesService,
  ]
})
export class TorrentsModule {
}
