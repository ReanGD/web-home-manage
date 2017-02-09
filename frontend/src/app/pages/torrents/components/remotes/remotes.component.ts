import {Component} from '@angular/core';
import {BaseTable} from '../../torrents.component';
import {TorrentsService, Remote} from '../../torrents.service';


@Component({
  selector: 'remotes-table',
  templateUrl: 'remotes.table.html',
})

export class RemotesTable extends BaseTable {

  torrents: Remote[];

  constructor(private service: TorrentsService) {
    super();
  }

  existTasks():boolean {
    for (let torrent of this.torrents) {
     if((torrent.local!=null) && (torrent.local.length!=0))
       return true;
    }

    return false;
  }

  refreshTable(by_timer = false) {
    this.service.getRemotes()
      .then(torrents => {
        this.torrents = torrents;
        super.refreshTableImpl(!by_timer, torrents.length);
      });
  }

  downloadTorrent(torrent: Remote) {
    this.service.createLocal(torrent)
      .then(() => this.refreshTable(true));
  }
}
