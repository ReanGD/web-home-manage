import {Component} from '@angular/core';
import {BaseTable} from '../../torrents.component';
import {TorrentsService, Local} from '../../torrents.service';


@Component({
  selector: 'locals-table',
  templateUrl: 'locals.table.html',
})

export class LocalsTable extends BaseTable {

  torrents: Local[];

  constructor(private service: TorrentsService) {
      super();
  }

  existTasks():boolean {
    for (let torrent of this.torrents) {
     if((torrent.task_id !=null) && (torrent.task_id.length!=0))
       return true;
    }

    return false;
  }

  refreshTable(by_timer = false) {
    this.service.getLocals()
      .then(torrents => {
        this.torrents = torrents;
        super.refreshTableImpl(!by_timer, torrents.length);
      });
  }

  removeTorrent(torrents: Local) {
    this.service.removeLocal(torrents)
      .then(() => this.refreshTable());
  }
}
