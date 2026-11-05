# Pruebas de concurrencia

Patrón para pruebas de carrera en el servicio de inscripción/cancelación.

## Base de clase

Usar `django.test.TransactionTestCase` (no `TestCase`) para permitir `atomic` real y rollback entre pruebas.

## Auxiliar de carrera (`race`)

```python
def race(self, calls):
    barrier = Barrier(len(calls))
    def worker(call):
        close_old_connections()
        try:
            database = str(connections["default"].settings_dict["NAME"])
            assert database.endswith("test.sqlite3"), database
            assert "memory" not in database, database
            barrier.wait(timeout=10)
            return call()
        finally:
            connections["default"].close()
    with ThreadPoolExecutor(max_workers=len(calls)) as executor:
        return list(executor.map(worker, calls))
```

- `Barrier` hace que todos los hilos arranquen al mismo tiempo.
- `close_old_connections()` + `connections["default"].close()` evitan compartir conexiones Django entre hilos.
- La base de pruebas debe ser un archivo real (`test.sqlite3`), no `:memory:`, para que el bloqueo de SQLite se aplique entre hilos.

## Reloj dentro del bloqueo

El servicio adquiere la reserva de escritura de SQLite (`IMMEDIATE`) al entrar al `atomic` y lee el instante real después. Para probar que el reloj se evalúa tras el lock, parchear `timezone.now` dentro del bloque:

```python
with patch("activities.services.timezone.now", side_effect=after_lock) as clock:
    self.assertEqual(register(student=..., activity_id=..., now=NOW), "started")
    clock.assert_called_once()
```

## Resultado esperado

Validar que nunca queden dos inscripciones vigentes del mismo alumno y actividad:

```python
current = Registration.objects.filter(student=..., activity=..., cancelled_at__isnull=True)
self.assertLessEqual(current.count(), 1)
```

## Resultado no esperado

No usar `TestCase` (evita `atomic` real), no compartir conexión entre hilos, no usar base `sqlite:///:memory:`.
