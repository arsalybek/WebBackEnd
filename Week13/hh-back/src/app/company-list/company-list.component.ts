import { Component, OnInit } from '@angular/core';
import {Company} from "../model";
import {CompanyService} from "../company.service";

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    this.getCompanyList();
  }

  getCompanyList(): void {
    this.companyService.getCompanyList().subscribe(companies => this.companies = companies);
  }

}
