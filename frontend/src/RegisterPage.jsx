import React from "react";
import { Form, Input, Button } from "antd";

const RegisterPage = () => {
  return (
    <div>
      <h2>Страница регистрации</h2>
      <Form>
        <Form.Item label="Имя">
          <Input />
        </Form.Item>
        <Form.Item label="Email">
          <Input type="email" />
        </Form.Item>
        <Form.Item label="Пароль">
          <Input.Password />
        </Form.Item>
        <Button type="primary">Зарегистрироваться</Button>
      </Form>
    </div>
  );
};

export default RegisterPage;
