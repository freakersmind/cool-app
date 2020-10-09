import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-list-product',
  templateUrl: './list-product.component.html',
  styleUrls: ['./list-product.component.css']
})
export class ListProductComponent implements OnInit {

  products;
  selectedProduct;
  constructor(public dataService: DataService) { }

  ngOnInit() {
    this.products = this.dataService.getProducts();
  }
  public selectProduct(product) {
    this.selectedProduct = product;
  }

}
