import {Component} from '@angular/core';

import 'style-loader!./torrents.scss';

@Component({
  selector: 'torrents',
  template: `<router-outlet></router-outlet>`
})


export class Torrents {
  constructor() {
  }
}
