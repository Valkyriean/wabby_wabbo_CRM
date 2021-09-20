<template>
    <Menu onClick={this.handleClick} selectedKeys={[current]} mode="horizontal">
        <Menu.Item key="Customers" disabled>
            View Customers
        </Menu.Item>
        <Menu.Item key="Forms" disabled>
            View Forms
        </Menu.Item>
        <Menu.Item key="login">
            <a href="https://ant.design" target="_blank" rel="noopener noreferrer">
            Login
            </a>
        </Menu.Item>
        <Menu.Item key="register">
            <a href="https://ant.design" target="_blank" rel="noopener noreferrer">
            Register
            </a>
        </Menu.Item>
    </Menu>
</template>