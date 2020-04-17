export interface Company {
  id: number;
  name: string;
  description: string;
  city: string;
  address: string;
}
export interface LoginResponse {
  token: string;
}
export interface Vacancy {
  id: number;
  name: string;
  description: string;
  salary: number;
  companyId: number;
}
