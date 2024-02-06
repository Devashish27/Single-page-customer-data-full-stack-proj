import React from "react";
import { render } from "@testing-library/react";
import CustomerList from "./CustomerList";

test('renders customer list', async () => {
    //  Mock the API call if needed
    // Render the component
    const { getByText } = render(<CustomerList />);

    // Add your test assertions..
    expect(getByText('Customer Management App')).toBeInTheDocument();
});

