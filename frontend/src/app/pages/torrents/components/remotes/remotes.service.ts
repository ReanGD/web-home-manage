import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import 'rxjs/add/operator/toPromise';
// import {Remotes} from '../domain/car';

export interface Remotes {
    id;
    name;
    ratio;
    finished;
    dir;
}


@Injectable()
export class RemotesService {

  constructor(private http: Http) {
  }

  getRemotes() {
    return this.http.get('http://127.0.0.1:8000/api/v1/remotes/')
                .toPromise()
                .then(res => <Remotes[]> res.json())
                .then(data => { return data; });
  }
}
