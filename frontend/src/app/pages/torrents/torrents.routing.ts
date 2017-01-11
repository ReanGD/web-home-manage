import { Routes, RouterModule }  from '@angular/router';

import { Tables } from './torrents.component';
import { BorderedTable } from './components/remoteView/remoteView.component';

// noinspection TypeScriptValidateTypes
const routes: Routes = [
  {
    path: '',
    component: Tables,
    children: [
      { path: 'remoteview', component: BorderedTable }
    ]
  }
];

export const routing = RouterModule.forChild(routes);
