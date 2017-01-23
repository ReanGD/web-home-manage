import { Routes, RouterModule }  from '@angular/router';

import { Torrents } from './torrents.component';
import { RemotesTable } from './components/remotes/remotes.component';

// noinspection TypeScriptValidateTypes
const routes: Routes = [
  {
    path: '',
    component: Torrents,
    children: [
      { path: 'remotes', component: RemotesTable }
    ]
  }
];

export const routing = RouterModule.forChild(routes);
