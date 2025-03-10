import { expect, test } from "vitest";

test('Adds two numbers', ()=>{
    const add = (a, b)=>{
        return a + b 
    }

    expect(add(2, 3)).toBe(5)
})