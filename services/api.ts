import axios from "axios";

const baseURL = "http://localhost:8000/api";

export const postCustomer = (data: any) => axios.post(`${baseURL}/customers/`, data);
export const getCustomers = () => axios.get(`${baseURL}/customers/`);
