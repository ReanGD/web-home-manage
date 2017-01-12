import { Routes, RouterModule }  from '@angular/router';

import { Torrents } from './torrents.component';
import { RemoveTorrentsTable } from './components/remoteView/remoteTorrents.component';

// noinspection TypeScriptValidateTypes
const routes: Routes = [
  {
    path: '',
    component: Torrents,
    children: [
      { path: 'remotetorrents', component: RemoveTorrentsTable }
    ]
  }
];

export const routing = RouterModule.forChild(routes);
