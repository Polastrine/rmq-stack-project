package com.producer.rabbitmq.producer_rabbitmq.web.controller;

import com.producer.rabbitmq.producer_rabbitmq.services.ProducerService;
import com.producer.rabbitmq.producer_rabbitmq.web.controller.dto.PedidoRequestDto;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/producer")
@RequiredArgsConstructor
public class ProducerController {
    private final ProducerService producerService;

    @PostMapping
    public ResponseEntity<String> enviar(@RequestBody PedidoRequestDto pedido){
        try {
            producerService.enviarPedido(pedido);
            return ResponseEntity.status(200).body("Pedido enviada com successo " + pedido.toString());
        }catch (Exception e){
            return ResponseEntity.status(400).body("Erro ao enviar pedido" + e.getMessage());
        }
    }
}
