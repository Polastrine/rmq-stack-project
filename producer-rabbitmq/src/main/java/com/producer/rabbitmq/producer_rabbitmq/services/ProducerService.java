package com.producer.rabbitmq.producer_rabbitmq.services;

import com.producer.rabbitmq.producer_rabbitmq.web.controller.dto.PedidoRequestDto;
import lombok.RequiredArgsConstructor;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ProducerService {

    private final RabbitTemplate rabbitTemplate;

    public void enviarPedido(PedidoRequestDto pedido){
        rabbitTemplate.convertAndSend(pedido);
    }
}
