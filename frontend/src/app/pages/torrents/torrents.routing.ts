import { Routes, RouterModule }  from '@angular/router';

import { Torrents } from './torrents.component';
import { RemotesTable } from './components/remotes/remotes.component';
import { LocalsTable } from './components/locals/locals.component';

// noinspection TypeScriptValidateTypes
const routes: Routes = [
  {
    path: '',
    component: Torrents,
    children: [
      { path: 'remotes', component: RemotesTable },
      { path: 'locals', component: LocalsTable }
    ]
  }
];

export const routing = RouterModule.forChild(routes);
