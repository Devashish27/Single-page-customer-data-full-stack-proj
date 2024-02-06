import React, { useEffect, useState } from "react";
import { getCustomers } from '../services/api';

interface Customer {
    id: number;
    name: string;
    // Add more properties needed.
}

const CustomerList: React.FC = () => {
    const [customers, setCustomers] = useState<Customer[]>([]);

    useEffect(() => {
        const fetchCustomers = async () => {
            try {
                const response = await getCustomers();
                setCustomers(response.data);
            } catch (error) {
                //Handle error.
            }
        };

        fetchCustomers();
    }, []);

    return (
        <div>
            {/* Display your customers */}
            {customers.map((customer) => (
                <div key={customer.id}>{customer.name}</div>
            ))}
        </div>
    );
};


export default CustomerList;
