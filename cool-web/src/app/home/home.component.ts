import { Component, OnInit } from '@angular/core';
import { EditorChangeContent, EditorChangeSelection } from 'ngx-quill'
import * as QuillNamespace from 'quill';
let Quill: any = QuillNamespace;
import ImageResize from 'quill-image-resize-module';
import { DataService } from '../data.service';
Quill.register('modules/imageResize', ImageResize);

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(public dataService: DataService) { }

  ngOnInit() {
  }

  fetchProducts() {
    this.dataService.getProducts();
  }


}
