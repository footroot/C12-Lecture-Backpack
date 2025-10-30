import { describe, expect, it } from "vitest";
import Ref from "./Ref";
import { screen, render } from "@testing-library/react"

describe('Ref Component', ()=>{
    it('Render Ref component', ()=>{
        render(<Ref/>)
        expect(screen.getByText(/Hello World/i)).toBeInTheDocument()
    })
})