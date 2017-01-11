import { Component, OnInit  } from '@angular/core';
import { BasicTablesService, Car } from './remoteView.service';

import 'style-loader!./remoteView.scss';

@Component({
  selector: 'bordered-table',
  templateUrl: './t.html',
})

export class BorderedTable implements OnInit {

  cars: Car[];

  constructor(private carService: BasicTablesService) { }

  ngOnInit() {
      // this.carService.getCarsSmall().then(cars => this.cars = cars);
      this.cars = this.carService.getCarsSmall();
  }
}
