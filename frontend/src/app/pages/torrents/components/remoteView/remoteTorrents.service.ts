import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import 'rxjs/add/operator/toPromise';
// import {RemoteTorrent} from '../domain/car';


export interface RemoteTorrent {
    id;
    name;
    ratio;
    finished;
    dir;
}


@Injectable()
export class RemoteTorrentsService {

  constructor(private http: Http) {
  }

  getRemoteTorrents() {
    return this.http.get('http://127.0.0.1:8000/api/v1/remote_torrents/')
                .toPromise()
                .then(res => <RemoteTorrent[]> res.json().results)
                .then(data => { return data; });
  }
}
