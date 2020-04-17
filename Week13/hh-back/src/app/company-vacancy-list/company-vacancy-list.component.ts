import { Component, OnInit } from '@angular/core';
import {CompanyService} from '../company.service';
import {ActivatedRoute} from '@angular/router';
import {Vacancy} from '../model';

@Component({
  selector: 'app-company-vacancy-list',
  templateUrl: './company-vacancy-list.component.html',
  styleUrls: ['./company-vacancy-list.component.css']
})
export class CompanyVacancyListComponent implements OnInit {
  vacancies: Vacancy[];
  constructor(private companiesService: CompanyService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getCompanyVacancies();
  }

  getCompanyVacancies(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companiesService.getCompanyVacancyList(id).subscribe(companyVacancies => this.vacancies = companyVacancies);
  }

}
