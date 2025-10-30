import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import Counter from "./Counter";

describe('Counter', ()=>{
    it('Increments value by 1', ()=>{
        render(<Counter />)
        fireEvent.click(screen.getByText(/Increment/i))
        expect(screen.getByText(/Count: 1/i)).toBeInTheDocument()
    })
})