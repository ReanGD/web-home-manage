import {Component, OnDestroy, OnInit} from '@angular/core';
import {Message, SelectItem} from "primeng/components/common/api";
import {Observable} from 'rxjs/Rx';
import {Subscription} from "rxjs/Subscription";

import 'style-loader!./torrents.scss';

@Component({
  selector: 'torrents',
  template: `<router-outlet></router-outlet>`
})


export class Torrents {
  constructor() {
  }
}

export abstract class BaseTable implements OnInit, OnDestroy {
  msgs: Message[] = [];
  content_type: SelectItem[];
  timer;
  subscription: Subscription;

  constructor() {
  }

  ngOnInit() {
    this.content_type = [];
    this.content_type.push({label: 'All', value: null});
    this.content_type.push({label: 'Films', value: 'Films'});
    this.content_type.push({label: 'AudioBooks', value: 'AudioBooks'});
    this.content_type.push({label: 'Serials', value: 'Serials'});
    this.content_type.push({label: 'Others', value: 'Others'});
    this.timer = Observable.timer(5000,5000);

    this.refreshTable(false);
  }

  abstract existTasks(): boolean;
  abstract refreshTable(by_timer);

  refreshTableImpl(show_message: boolean, count_line: number) {
    if(this.existTasks()) {
      if (this.subscription == null)
        this.subscription = this.timer.subscribe(t => this.refreshTable(true));
    }
    else {
      if (this.subscription != null) {
        this.subscription.unsubscribe();
        this.subscription = null;
      }
      show_message = true;
    }

    if (show_message) {
      let msg = {
        severity: 'success',
        summary: 'Load success',
        detail: count_line + ' torrents'
      };
      this.msgs.push(msg);
    }
  }

  ngOnDestroy() {
    if (this.subscription != null)
      this.subscription.unsubscribe();
  }
}
