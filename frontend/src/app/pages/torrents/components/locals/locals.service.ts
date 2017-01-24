import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import 'rxjs/add/operator/toPromise';

export interface Remotes {
  name;
  content_type;
  dir;
  files;
}

export interface Locals {
  id;
  remote: Remotes;
}

@Injectable()
export class LocalsService {

  constructor(private http: Http) {
  }

  get() {
    return this.http.get('http://127.0.0.1:8000/api/v1/locals/')
                .toPromise()
                .then(res => <Locals[]> res.json())
                .then(data => { return data; });
  }
}
