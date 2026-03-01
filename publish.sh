#!/bin/bash
echo "Subiendo cambios a GitHub..."
git push --set-upstream origin main
if [ $? -eq 0 ]; then
    echo "¡Cambios subidos exitosamente!"
else
    echo "Hubo un error al subir los cambios. Revisa tu conexión o autenticación."
fi
