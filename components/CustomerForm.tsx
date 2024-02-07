import React, { useState } from 'react';
import { postCustomer } from '../services/api';

const CustomerForm: React.FC = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
      console.log('Form submitted:', formData);

    try {
      await postCustomer(formData);
          console.log('Data sent successfully!');

      setFormData({
        name: '',
        email: '',
        phone: '',
      });

    } catch (error) {
      console.error('Error submitting customer data:', error);
          console.error('Error sending data:', error);

    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" name="name" value={formData.name} onChange={handleInputChange} />
      </label>
      <label>
        Email:
        <input type="text" name="email" value={formData.email} onChange={handleInputChange} />
      </label>
      <label>
        Phone:
        <input type="text" name="phone" value={formData.phone} onChange={handleInputChange} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
};

export default CustomerForm;
