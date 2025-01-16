import { useState } from 'react'
import { useName } from './userContext'

function Welcome() {
    let name = useName();
    return (
        <div>
            <h1>
                Welcome to our app, {name}!
            </h1>
        </div>
    )
}

export default Welcome
