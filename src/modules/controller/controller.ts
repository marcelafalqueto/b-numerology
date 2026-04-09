import { Request, Response } from "express";

import { NumerologicMapRequestDTO, PurchaseInputDTO } from "@/modules/dto/dto";

import { NumerologyCalculatorService } from "@/modules/service/generateMap";

const numerologicCalculatorService = new NumerologyCalculatorService();

export const numerologicMapController = (req: Request, res: Response) => {
    const { language, name, birth_date } = req.body as NumerologicMapRequestDTO;

    const numerologyMap = numerologicCalculatorService.getNumerologyMap(language, name, birth_date);

    return res.json(numerologyMap);
};

export const createPurchaseController = (req: Request<{}, {}, PurchaseInputDTO>, res: Response) => {
    req.body.userId;
    req.body.language;
    req.body.mapData;
    res.json({ ok: true });
};
