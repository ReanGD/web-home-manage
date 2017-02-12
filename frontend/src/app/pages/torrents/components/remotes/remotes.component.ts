import {Component} from '@angular/core';
import {ConfirmationService} from "primeng/primeng";
import {BaseTable} from '../../torrents.component';
import {TorrentsService, Remote} from '../../torrents.service';


@Component({
  selector: 'remotes-table',
  templateUrl: 'remotes.table.html',
  providers: [ConfirmationService],
})

export class RemotesTable extends BaseTable {

  torrents: Remote[];

  constructor(private service: TorrentsService, private confirmationService: ConfirmationService) {
    super();
  }

  existTasks(): boolean {
    for (let torrent of this.torrents) {
      if ((torrent.local != null) && (torrent.local.length != 0))
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
    this.confirmationService.confirm({
      message: 'Are you sure that you want to load "' + torrent.name + '"?',
      accept: () => {
        this.service.createLocal(torrent)
          .then(() => this.refreshTable(true));
      }
    });
  }
}
