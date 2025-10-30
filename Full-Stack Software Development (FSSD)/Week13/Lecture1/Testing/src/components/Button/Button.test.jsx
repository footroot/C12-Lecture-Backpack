import { render, screen } from "@testing-library/react";
import { describe, expect, it, test } from "vitest";
import Button from "./Button";

describe('Button', ()=>{
    it('Render correctly', ()=>{
        render(<Button/>)
        expect(screen.getByText(/Clicked Me/i)).toBeInTheDocument()
    })

})
