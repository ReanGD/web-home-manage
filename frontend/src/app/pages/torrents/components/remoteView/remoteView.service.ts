import {Injectable} from '@angular/core';
import {Http, Response} from '@angular/http';
// import {Car} from '../domain/car';


export interface Car {
    vin;
    year;
    brand;
    color;
}


@Injectable()
export class BasicTablesService {

  constructor(private http: Http) {
  }

  getCarsSmall() {
    return <Car[]> {
      "data": [
        {"brand": "VW", "year": 2012, "color": "Orange", "vin": "dsad231ff"},
        {"brand": "Audi", "year": 2011, "color": "Black", "vin": "gwregre345"},
        {"brand": "Renault", "year": 2005, "color": "Gray", "vin": "h354htr"},
        {"brand": "BMW", "year": 2003, "color": "Blue", "vin": "j6w54qgh"},
        {"brand": "Mercedes", "year": 1995, "color": "Orange", "vin": "hrtwy34"},
        {"brand": "Volvo", "year": 2005, "color": "Black", "vin": "jejtyj"},
        {"brand": "Honda", "year": 2012, "color": "Yellow", "vin": "g43gr"},
        {"brand": "Jaguar", "year": 2013, "color": "Orange", "vin": "greg34"},
        {"brand": "Ford", "year": 2000, "color": "Black", "vin": "h54hw5"},
        {"brand": "Fiat", "year": 2013, "color": "Red", "vin": "245t2s"}
      ]
    }.data;

    // return this.http.get('/showcase/resources/data/cars-small.json')
    //             .toPromise()
    //             .then(res => <Car[]> res.json().data)
    //             .then(data => { return data; });
  }
}
