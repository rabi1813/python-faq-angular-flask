import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class CommonServiceService {

  rootURL = "http://127.0.0.1:5000"
  constructor(private http: HttpClient) { }

  getDataType() {
    const url = this.rootURL + '/data_type'
    return this.http.get(url);
  }
}
