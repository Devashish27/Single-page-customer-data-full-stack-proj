import React from "react";
import { render } from "@testing-library/react";
import CustomerList from "./CustomerList";

test('renders customer list', async () => {
    const { getByText } = render(<CustomerList />);

    expect(getByText('Customer Management App')).toBeInTheDocument();
});

