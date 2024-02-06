import React from 'react';
import CustomerForm from './components/CustomerForm';
import CustomerList from './components/CustomerList';

const App: React.FC = () => {
  return (
    <div>
      <h1>
        Customer Object Management
      </h1>
      <CustomerForm />
      <CustomerList />
    </div>
  );
};

export default App;
