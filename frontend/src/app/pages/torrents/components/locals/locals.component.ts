import {Component} from '@angular/core';
import {ConfirmationService} from "primeng/primeng";
import {BaseTable} from '../../torrents.component';
import {TorrentsService, Local} from '../../torrents.service';


@Component({
  selector: 'locals-table',
  templateUrl: 'locals.table.html',
  providers: [ConfirmationService],
})

export class LocalsTable extends BaseTable {

  torrents: Local[];

  constructor(private service: TorrentsService, private confirmationService: ConfirmationService) {
    super();
  }

  existTasks(): boolean {
    for (let torrent of this.torrents) {
      if ((torrent.task_id != null) && (torrent.task_id.length != 0))
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

  removeTorrent(torrent: Local) {
    this.confirmationService.confirm({
      message: 'Do you want to delete "' + torrent.remote.name + '"?',
      header: 'Delete Confirmation',
      icon: 'fa fa-trash',
      accept: () => {
        this.service.removeLocal(torrent)
          .then(() => this.refreshTable(true));
      }
    });
  }
}
