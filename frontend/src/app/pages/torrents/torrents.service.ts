import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
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
      .then(res => <Remotes[]> res.json())
      .then(data => {
        return data;
      });
  }

  getLocals() {
    return this.http.get('http://127.0.0.1:8000/api/v1/locals/')
                .toPromise()
                .then(res => <Locals[]> res.json())
                .then(data => { return data; });
  }

  createLocals(torrent: Remotes) {
    alert(torrent.name+'=='+torrent.id);
  }
}
