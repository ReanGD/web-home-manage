import {Injectable} from '@angular/core';
import {Http, Headers} from '@angular/http';
import 'rxjs/add/operator/toPromise';

export interface Remotes {
  id;
  name;
  content_type;
  ratio;
  finished;
  dir;
  files;
}

export interface RemotesShort {
  name;
  content_type;
  dir;
  files;
}

export interface Locals {
  id;
  remote: RemotesShort;
}

@Injectable()
export class TorrentsService {

  constructor(private http: Http) {
  }

  getRemotes() {
    return this.http.get('http://127.0.0.1:8000/api/v1/remotes/')
      .toPromise()
      .then(res => {
        return <Remotes[]> res.json();
      });
  }

  getLocals() {
    return this.http.get('http://127.0.0.1:8000/api/v1/locals/')
      .toPromise()
      .then(res => {
        return <Locals[]> res.json();
      });
  }

  createLocals(torrent: Remotes) {
    var headers = new Headers({
      'Content-Type': 'application/json'
    });
    var data = JSON.stringify({'id': torrent.id});

    return this.http.post('http://127.0.0.1:8000/api/v1/locals/',
      data,
      {headers: headers})
      .toPromise()
      .then(res => {
        return <Locals> res.json();
      });
  }
}
