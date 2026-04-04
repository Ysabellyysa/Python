FROM quay.io/astronomer/astro-runtime:12.6.0

# Vira administrador para instalar ferramentas do sistema
USER root
RUN apt-get update && apt-get install -y default-jre procps

# Volta para o usuário padrão do Airflow
USER astro
