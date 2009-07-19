# New ports collection makefile for:    py-scrpy
# Date created:                         10 Jul 2009
# Whom:                                 Qing Feng <qingfeng@me.com>
#
# $FreeBSD$
#

PORTNAME=	scrpy
PORTVERSION=	0.8
CATEGORIES=	www python
MASTER_SITES=	http://hg.scrapy.org/scrapy/archive/
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	tip
EXTRACT_SUFX=	.zip

MAINTAINER=	qingfeng@me.com
COMMENT=	Scrapy is a high level scraping and web crawling framework for writing spiders to crawl and parse web pages for all kinds of purposes, from information retrieval to monitoring or testing web sites.

BUILD_DEPENDS=	${PYTHON_SITELIBDIR}/twisted:${PORTSDIR}/devel/py-twistedCore
BUILD_DEPENDS=	${PYTHON_SITELIBDIR}/libxml2:${PORTSDIR}/textproc/py-libxml2
#LIB_DEPENDS=    xml2:${PORTSDIR}/textproc/libxml2
RUN_DEPENDS=	${BUILD_DEPENDS}
WRKSRC=		${WRKDIR}/scrapy-963e6fd4c371

USE_PYTHON=		yes
USE_PYDISTUTILS=	yes

.include <bsd.port.mk>
